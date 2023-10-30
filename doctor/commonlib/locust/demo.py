from locust import HttpUser, task


class HelloWorldUser(HttpUser):

    @task
    def hello_world(self):
        self.client.get("/v1/portraits/dbs?page.limit=100")
        i = 1