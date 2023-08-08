# Pull the official base image
FROM node:14

# Set working directory in the Docker container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install the dependencies
RUN npm install

# Bundle app source
COPY . .

RUN npm install cors

# Expose the port the app runs in
EXPOSE 3000

# Serve the app
CMD ["node", "server.js"]