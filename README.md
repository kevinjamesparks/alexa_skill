![alt text](https://ask-toolkit.gallerycdn.vsassets.io/extensions/ask-toolkit/alexa-skills-kit-toolkit/0.2.1/1533049618020/Microsoft.VisualStudio.Services.Icons.Default)
# Alexa Skill

## Getting Started

Here is some information on how to install dependencies and run the application

### Prerequisite

[Python 3](https://www.python.org/downloads/) is required for this application

### Add control file to path
Add the 'run' bash file to path so `run` command can be used
```
export PATH=$PATH:<root/folder/of/application>
```

### Installing

```
run setup
```

## Running the development server

With `run` 
```
run start
```

Running the skill behind https with ngrok
```
ngrok http 5000
```
ngrok makes it so Alexa can talk to your code right away.\
Use the HTTPS endpoint on Amazon's developer portal


## Authors

* **Kevin James parks**