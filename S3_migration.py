import boto3
import os
 
def process_files(event, context):
    # Set the S3 client
    s3 = boto3.client('s3')
 
    # Define constants for bucket and fixed part of the path
    source_bucket_name = 'your-source-bucket-name'
    base_path = ''  
    target_bucket_name = 'your-target-bucket-name'
    
 
    # Initialize a list to keep track of processed files
    files_processed = []
 
    # Process each file uploaded to the bucket
    for record in event['Records']:
        object_key = record['s3']['object']['key']
        # Ensure the object key starts with the base path
        if object_key.startswith(base_path):
            # Extract the specific subfolder (e.g., '123')
            subfolder_path = object_key[len(base_path):].split('/')[0]
            # Check if the file is a PDF or TIFF
            if object_key.lower().endswith(('.pdf', '.tiff')):
                # Get the file content
                file_obj = s3.get_object(Bucket=source_bucket_name, Key=object_key)
                file_content = file_obj['Body'].read()
 
                # Extract file name and extension
                file_name, file_ext = os.path.splitext(os.path.basename(object_key))
 
                # Create a new file name with the subfolder name appended
                new_file_name = f"{file_name}_{subfolder_path}{file_ext}"
 
                # Upload the modified file to the target bucket
                s3.put_object(Body=file_content, Bucket=target_bucket_name, Key=os.path.join(subfolder_path, new_file_name))
 
                # Optionally, delete the original file
                s3.delete_object(Bucket=source_bucket_name, Key=object_key)
 
                # Log the processed file
                files_processed.append(object_key)

 
    return {
        'statusCode': 200,
        'body': f"Successfully processed {len(files_processed)} files: {files_processed}"
    }

