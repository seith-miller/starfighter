
# install os dependences 
apt-get update && apt-get install -y -t unstable \
git \
libssl-dev \
r-base-dev \
r-recommended \
sudo \
gdebi-core \
pandoc \
pandoc-citeproc \
libcurl4-gnutls-dev \
libcairo2-dev/unstable \
libxt-dev \
subversion \
libgdal-dev \
libproj-dev \
libv8-dev

# install r devtools
install2.r --error \
devtools

# Download and install shiny server
wget --no-verbose https://s3.amazonaws.com/rstudio-shiny-server-os-build/ubuntu-12.04/x86_64/VERSION -O "version.txt" && \
VERSION=$(cat version.txt)  && \
wget --no-verbose "https://s3.amazonaws.com/rstudio-shiny-server-os-build/ubuntu-12.04/x86_64/shiny-server-$VERSION-amd64.deb" -O ss-latest.deb && \
gdebi -n ss-latest.deb && \
rm -f version.txt ss-latest.deb && \
R -e "install.packages(c('shiny', 'rmarkdown'), repos='https://cran.rstudio.com/')" && \
cp -R /usr/local/lib/R/site-library/shiny/examples/* /srv/shiny-server/

# Install devtools and leaflet
R -e "install.packages('devtools'); library(devtools)" && \
R -e "library(devtools); devtools::install_github('rstudio/leaflet')"

# Install R packages
R -e "install.packages('rjson', repos='http://cran.rstudio.com/')" && \
R -e "install.packages('maps', repos='http://cran.rstudio.com/')" && \
R -e "install.packages('raster', repos='http://cran.rstudio.com/')" && \
R -e "install.packages('dismo', repos='http://cran.rstudio.com/')" && \
R -e "install.packages('shinythemes', repos='http://cran.rstudio.com/')" && \
R -e "install.packages('rgdal', repos='http://cran.rstudio.com/')" && \
R -e "install.packages('devtools', repos='http://cran.rstudio.com/')" && \
R -e "install.packages('rgbif', repos='http://cran.rstudio.com/')" && \
R -e "install.packages('shinydashboard', repos='http://cran.rstudio.com/')" && \
R -e "install.packages('randomForest', repos='http://cran.rstudio.com/')" && \
R -e "install.packages('kernlab', repos='http://cran.rstudio.com/')" && \
R -e "install.packages('rJava', repos='http://cran.rstudio.com/')" && \
R -e "install.packages('rgeos', repos='http://cran.rstudio.com/')" && \
R -e "install.packages('shinyBS', repos='http://cran.rstudio.com/')" && \
R -e "install.packages('doBy', repos='http://cran.rstudio.com/')" && \
R -e "install.packages('ggplot2', repos='http://cran.rstudio.com/')"

COPY shiny-server.sh /usr/bin/shiny-server.sh

sh /usr/bin/shiny-server.sh
