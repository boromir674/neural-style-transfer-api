from fastapi import APIRouter, File, UploadFile, Depends, WebSocket
from fastapi.responses import StreamingResponse, Response, FileResponse

from pydantic import BaseModel
from typing import Optional, Callable, Tuple, Protocol, Dict, Any
import asyncio

from neural_style_transfer_api.nst import get_algo_n_subscriber

class ProgressState(Protocol):
    # metrics is a dict with the 'iterations' key
    metrics: Dict[str, Any]
   

class Progress(Protocol):
    state: ProgressState


class ProgressListener(Protocol):
    """Designed to be called on every nst epoch."""
    def update(self, progress: Progress, *args, **kwargs) -> None:
        """Update the progress listener with the current progress."""
        ...


GetAlgoNSubscriber = Callable[[int, str, float], Tuple[Callable[[str, str], None], Callable[[ProgressListener], None]]]
# def get_algo_n_subscriber(iterations: int, location: str, noisy_ratio: float = 0.6) -> t.Tuple[t.Callable[[str, str], None], t.Callable[[ProgressListener], None]]:
def get_get_algo_n_subscriber() -> GetAlgoNSubscriber:
    return get_algo_n_subscriber


router = APIRouter()


class NSTParams(BaseModel):
    ratio: Optional[float] = 0.6
    iterations: Optional[int] = 10


# class NSTResponse(BaseModel):

@router.post(
    "/nst-rest",
    # Set what the media type will be in the autogenerated OpenAPI specification.
    # fastapi.tiangolo.com/advanced/additional-responses/#additional-media-types-for-the-main-response
    responses = {
        200: {
            "content": {"image/png": {}}
        }
    },

    # Prevent FastAPI from adding "application/json" as an additional
    # response media type in the autogenerated OpenAPI specification.
    # https://github.com/tiangolo/fastapi/issues/3258
    response_class=FileResponse,
)
async def neural_style_transfer_endpoint(
    content_image: UploadFile = File(...),
    style_image: UploadFile = File(...),
    params: NSTParams = Depends(NSTParams),
    # iterations: int, location: str, noisy_ratio: float = 0.6) -> t.Tuple[t.Callable[[str, str], None], t.Callable[[ProgressListener], None]]
    # get_algo_n_subscriber: Callable[[int, str, float], None] = Depends(get_get_algo_n_subscriber),
    get_algo_n_subscriber: GetAlgoNSubscriber = Depends(get_get_algo_n_subscriber),
):
    # Save uploaded images
    # content_path = f"/content_images/content_{content_image.filename}"
    # style_path = f"/style_images/style_{style_image.filename}"
    content_path = f"/tmp/{content_image.filename}"
    style_path = f"/tmp/{style_image.filename}"

    with open(content_path, "wb") as content_file:
        content_file.write(content_image.file.read())

    with open(style_path, "wb") as style_file:
        style_file.write(style_image.file.read())

    # use the artificial_artowrk objects to setup and run nst
    nst_runner, subscribe_callback = get_algo_n_subscriber(
        params.iterations,
        "/tmp",
        params.ratio,
    )

    # run nst in the foreground
    nst_runner(
        content_path,  # local to server
        style_path,  # local to server
    )

    # if image is in bytes in memory already, then
    # return Response(content=image_bytes, media_type="image/png")
    
    image_path: str = f"/tmp/{content_image.filename}+{style_image.filename}-{params.iterations}.png"
    return FileResponse(image_path, media_type="image/png")