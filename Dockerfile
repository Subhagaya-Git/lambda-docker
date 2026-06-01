FROM public.ecr.aws/lambda/python:3.12

# Copy function code... LAMBDA_TASK_ROOT is /var/task, the working directory set in the base image
COPY lambda_function.py ${LAMBDA_TASK_ROOT}    

# Set the CMD to your handler - lambda_handler
CMD ["lambda_function.lambda_handler"]       