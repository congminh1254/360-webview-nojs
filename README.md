# Streetview

## Introduction

### Purpose of the project
The aim of the project is to create free and open-source software that allows viewing a set of spherical photos in a web browser, including devices with low computing power, mobile devices, devices with limited Internet access and browsers without JavaScript support.

### Initial vision of the project
As the project is not to use javascript, the following buttons will be used for "rotating": up, down, right, left. Clicking the button will render the image slightly rotated in the desired direction.

### The nature of the problem
The problem of this project is to convert the input photo (equidistant projection) to the normal field of view (Both photos are in jpg format).

## Installation guide
Instructions for the administrator how to install the project:
1. Clone the repository from https://github.com/congminh1254/360-webview-nojs to your local machine.
2. Download and unzip the 360 degree photo dataset on your host computer.
3. Open a terminal and navigate to the root directory of the cloned repository.
4. To clear the previous Docker container, run the following command:
```
docker stop 360-webview && docker rm 360-webview
```
5. To compile the current version of the project into a Docker image, run the following command:
```
docker build . -t 360-webview
```
6. To deploy a Docker container with the dataset directory mounted in /python-docker/data, run the following command:
```
docker run -d -it --name 360-webview --restart always --mount type=bind,source=$HOME/data_folder,target=/python-docker/data -p 9001:9001 360-webview
```
This command will start a Docker container named `360-webview` which will automatically restart after rebooting the system (`--restart always`). It will also mount the dataset directory located in `$HOME/data_folder` in the `/python-docker/data` directory of the container where the application will look for 360 degree photos.

Finally, it will map port 9001 of the container to port 9001 of the host (`-p 9001:9001`) where the application will be accessible from the web browser.

7. Optional: To configure Nginx to proxy traffic from the Internet to port 9001, follow these steps:
     - Install Nginx if it is not already installed on your system.
     - Open the Nginx configuration file, usually located in `/etc/nginx/nginx.conf`, with a text editor.
     - Add the following code block in the `http` block:
       ```
        server {
          listen 80;
          server_name example.com;
          location / {
              proxy_pass http://localhost:9001;
              proxy_set_header Host $host;
              proxy_set_header X-Real-IP $remote_addr;
              proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
          }
        }
       ```
     - Replace `example.com` with your domain name or IP address.
     - Save and close the file, then restart Nginx with the following command:
       ```
       sudo systemctl restart nginx
       ```
     - Now you should be able to access the app from your web browser by going to "http://example.com" or your IP address.
