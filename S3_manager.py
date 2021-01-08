# -*- coding: utf-8 -*-
import boto3

class S3Manager:
    def __init__(self, region_name=None):
        if region_name is None:
            self.s3 = boto3.resource('s3')
        else:
            self.s3 = boto3.resource('s3', region_name=region_name)
            
    def exists(self, bucket_name, key):
        bucket = self.s3.Bucket(bucket_name)
        objects = list(bucket.objects.filter(Prefix=key))

        if objects and objects[0].key == key:
            return True

        return False

    def download_data(self, bucket_name, key, download_path):
        bucket = self.s3.Bucket(bucket_name)
        objects = list(bucket.objects.filter(Prefix=key))

        if objects and objects[0].key == key:
            bucket.download_file(objects[0].key, download_path)
            return True

        return False

    def delete_file(self, bucket_name, key):
        print('delete_file')
        self.s3.meta.client.delete_object(Bucket=bucket_name, Key=key)

    def upload_file(self, bucket_name, key, localpath):
        print('upload_file')
        self.s3.meta.client.upload_file(localpath, bucket_name, key)
