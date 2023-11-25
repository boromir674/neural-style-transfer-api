"""Client code for running artificial_artwork nst algorithm."""
import typing as t


from artificial_artwork._main import create_algo_runner

class ProgressState(t.Protocol):
    # metrics is a dict with the 'iterations' key
    metrics: t.Dict[str, t.Any]
   

class Progress(t.Protocol):
    state: ProgressState


class ProgressListener(t.Protocol):
    """Designed to be called on every nst epoch."""
    def update(self, progress: Progress, *args, **kwargs) -> None:
        """Update the progress listener with the current progress."""
        ...


def get_algo_n_subscriber(iterations: int, location: str, noisy_ratio: float = 0.6) -> t.Tuple[t.Callable[[str, str], None], t.Callable[[ProgressListener], None]]:
    backend_objs: t.Dict[str, t.Any] = create_algo_runner(
        iterations=iterations,
        output_folder=location,
        noisy_ratio=noisy_ratio,
    )
    run_nst: t.Callable[[str, str], None] = backend_objs["run"]
    subscribe_callback: t.Callable[[ProgressListener], None] = backend_objs['subscribe']
    return run_nst, subscribe_callback

    # run_nst(content_image_path, style_image_path)


# backend_objs: t.Dict[str, t.Any] = create_algo_runner(
#     iterations=iterations,
#     output_folder=location,
#     noisy_ratio=0.6,
# )
# run_nst: t.Callable[[str, str], None] = backend_objs["run"]
# # subscribe_callback: t.Callable[[HandleAlgorithmProgressUpdatesAble], None] = backend_objs['subscribe']

# def update(self, *args, **kwargs) -> None:
#     self.runtime_state = args[0].state.metrics[
#         cls.mapping[termination_type]["key_name"]
#     ]