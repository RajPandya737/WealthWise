To get started contributing, ensure you have the required tools installed. 

[Node](https://nodejs.org/en/download/).
[Python](https://www.python.org/downloads/).
[Docker](https://www.docker.com/products/docker-desktop).

Once you have installed Docker Desktop, open the application and ensure that it starts without any issues. Additionally, if you are using VSCode, you can install the Docker extension to manage your containers.

Once you have the required tools installed, clone the repository to your local machine and open the project (wealthwise folder) in your preferred code editor.
    
```
git clone https://github.com/RajPandya737/WealthWise.git
```


To check if everything is working, we need to run the backend and frontend servers. 

Then, run the following commands to test the backend:
```
cd backend\dashboard_backend
```
```
docker-compose build
```
```
docker-compose up
```

Navigate to [http://localhost:8000/](http://localhost:8000/) in your browser. You should see a screen that is not an error page. This indicates that the backend is running successfully.


On your Docker Desktop, navigate to the "Images" tab and you should see a new image called "backend_web" and "postgres". This is a good sign. Navigate back to your terminal and stop the backend (Ctrl + C) and run the following command to start testing the frontend:

```
cd ../wealthwise
```
```
npm run dev
```
The front server should now be running, navigate the link in the terminal ([http://localhost:3000](http://localhost:8000/)) and you should see a screen that is not an error page.


If you have reached this point, you have successfully set up the project and are ready to start contributing. 