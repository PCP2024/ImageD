FROM python:3.12

# Set working directory
WORKDIR /app

# # Install system dependencies for PyQt6 $ VNC
# RUN apt-get update && apt-get install -y \
#     libgl1-mesa-glx \
#     libglib2.0-0 \
#     libegl1 \
#     libxkbcommon-x11-0 \
#     x11vnc \
#     xvfb \
#     fluxbox \
#     wget \
#     # python3-pyqt6 \
#     x11-apps \
#     libgl1-mesa-glx \
#     libegl1-mesa \
#     libqt6core6 \
#     libqt6gui6 \
#     libqt6widgets6 \
#     && rm -rf /var/lib/apt/lists/*

# Install noVNC to access the VNC server via a web browser
# RUN mkdir -p /usr/share/novnc && \
#     wget -qO- https://github.com/novnc/noVNC/archive/refs/tags/v1.5.0.tar.gz | tar xz --strip 1 -C /usr/share/novnc && \
#     ln -s /usr/share/novnc/vnc_lite.html /usr/share/novnc/index.html

# # Set the DISPLAY environment variable
# ENV DISPLAY=host.docker.internal:0

# Set up the VNC server environment
# ENV DISPLAY=:0
# RUN Xvfb :0 -screen 0 1024x768x16 & \
#     x11vnc -passwd your_password -display :0 -N -forever & \
#     fluxbox &

# RUN apt-get update && apt-get install -y \
#     libgl1-mesa-glx \
#     libglib2.0-0 \
#     libegl1 \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*


# Install the application dependencies
# COPY requirements.txt .
COPY requirements_docker.txt .
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements_docker.txt
# RUN python -m pip install --no-cache-dir -r requirements.txt

# Copy in the whole code
COPY . /app


# Expose the VNC server port
# EXPOSE 5900

# Expose the noVNC web port
# EXPOSE 6081

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["python", "ImageD_GUI.py"]
# CMD ["/usr/share/novnc/utils/novnc_proxy", "--vnc", "localhost:5900", "--listen", "localhost:6081"]
