#base image
FROM python
COPY . /Ass
WORKDIR /Ass
CMD python pyfile.py
