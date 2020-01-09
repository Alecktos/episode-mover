import asyncio

from memover import watcher
from . import arguments_parser
from . import logger
from . import mover


def main():
    args = arguments_parser.get_args()

    if args.type == arguments_parser.Commands.BY_NAME:
        mover.move_media_by_name(
            args.media_name,
            args.source,
            args.show_destination,
            args.movie_destination
        )
        return

    if args.type == arguments_parser.Commands.BY_PATH:
        mover.move_media_by_path(
            args.source,
            args.show_destination,
            args.movie_destination
        )
        return

    if args.type == arguments_parser.Commands.WATCH:
        asyncio.run(watcher.main())
        return

    logger.log('No action was made')
