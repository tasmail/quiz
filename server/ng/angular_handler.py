from tornado.web import StaticFileHandler, HTTPError


class AngularHandler(StaticFileHandler):
    async def get(self, path=None, include_body=True):
        if not path:
            path = 'index.html'

        try:
            res = await super().get(path, include_body)
        except HTTPError as e:
            if not e.status_code == 404:
                raise

            res = await super().get('index.html', include_body)

        return res
