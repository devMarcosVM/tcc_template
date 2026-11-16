FROM debian:buster-slim
FROM debian:bookworm-slim

RUN apt-get update
RUN apt-get install -y ghostscript texlive-publishers texlive-lang-portuguese texlive-latex-extra texlive-fonts-recommended make texlive-font-utils texlive-extra-utils
RUN apt-get install python3-pip -y
RUN pip3 install Pygments
RUN apt-get update && apt-get install -y latexmk
RUN apt-get update && apt-get install -y --no-install-recommends \
    ghostscript \
    texlive-publishers \
    texlive-lang-portuguese \
    texlive-latex-extra \
    texlive-fonts-recommended \
    texlive-font-utils \
    texlive-extra-utils \
    latexmk \
    make \
    python3-pygments \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /home/latex

