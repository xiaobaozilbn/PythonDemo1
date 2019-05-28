import cherrypy
class StaticPage():
    
    @cherrypy.expose
    def index(self):
        return open('\ cpts_1641_dxe \index.html')
        
if __name__ == '__main__':
        # cherrypy.config.update(conf)
    cherrypy.config.update({'server.socket_port': 9098})
    cherrypy.quickstart(StaticPage())
    