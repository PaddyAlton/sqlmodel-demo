FROM python:3.10-slim

# create a non-root user/usergroup
RUN addgroup --gid 10001 --system nonroot \
 && adduser  --uid 10000 --system --ingroup nonroot --home /demo demo-user

# switch working directory to non-root user's home
WORKDIR /demo

# install our dependencies
RUN python3 -m pip install -U pip && pip install pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --three --system

# add the working directory to the PYTHONPATH
ENV PYTHONPATH="${PYTHONPATH}:/demo"

# shouldn't run the application as root
USER demo-user

# bring in the source code
COPY src src

# run the application
ENTRYPOINT ["uvicorn", "src:app"]
CMD ["--host", "0.0.0.0", "--port", "8765"]
