# base image to be used
FROM python:3.9

# The environment variable ensures that the python output is set 
#straight to the terminal with out buffering it first
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /django

# add the requirements file to the working dir
COPY /requirements.txt /django/

# upgrade the pip
RUN pip3 install --upgrade pip

#install the requirements (install before adding rest of code to #avoid rerunning this at every code change-built in layers)
RUN pip3 install -r requirements.txt

# Copy the current directory contents into the container at /django/
COPY . /django/

#port from the container to expose to host
EXPOSE 8000

#Tell image what to do when it starts as a container
RUN chmod +x /django/start.sh

# run the sh file
CMD /django/start.sh