class Director:


    def _do_outputs(self,cast):
        self._video_service.get_all_actors()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
