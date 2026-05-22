from locust import HttpUser, task, between


class Yuk_testim(HttpUser):
    wait_time = between(1, 5)

    @task
    def test_login(self):
        self.client.get("/get")

 
    @task(2) #bu test 2 kat daha fazla çalışacak
    def Yuk_testim2(self):
        self.client.get("/get2")