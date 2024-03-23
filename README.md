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

First install python packages:
```bash
pip install -r requirements.txt
```

Then, run the following command to test the backend:
```bash
python backend/app.py
```

Navigate to [http://localhost:5000/test](http://localhost:5000/test) in your browser. You should see a screen that is not an error page. This indicates that the backend is running successfully.

go to the frontend directory (from root directory):
```bash
cd wealthwise
```

install node modules:
```bash
npm i
```
Run servers:
```bash
npm run dev
```
The front server should now be running, navigate the link in the terminal ([http://localhost:3000](http://localhost:3000/)) and you should see a screen that is not an error page.


If you have reached this point, you have successfully set up the project and are ready to start contributing. Currently we are not using docker, however, we may do so in the future
