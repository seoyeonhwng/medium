#!/bin/bash

# test.zip 파일이 존재하면 삭제
echo 'packaging test function ...'
if [ -f "test.zip" ]; then
    rm test.zip
fi

# 마지막 커밋, 현재 날짜, 호스트 이름
commit_hash="$(git log --format='%H' HEAD -n1)"
now="$(date +'%Y-%m-%d %H:%M')"
hostname="$(hostname)"

# build.sh 실행
sh ./build.sh
if [ $? != 0 ]; then
    echo "패키지 빌드에 실패하였습니다. 배포를 중단합니다."
    exit 1
fi

# 생성된 package.zip을 test.zip으로 이름 변경
mv package.zip test.zip
echo "packaging done"

# test.zip파일을 S3로 업로드
echo "uploading test.zip to S3..."
aws s3 cp test.zip s3://lambda-function-support/
echo "upload done"

# s3에서 람다로 코드 배포
echo "deploying test function to Lambda"
aws lambda update-function-code --function-name test --s3-bucket lambda-function-support --s3-key test.zip
aws lambda publish-version --function-name test --description "$now (from $hostname) @$commit_hash"
echo "deploy done"

if [ -f "test.zip" ]; then
    rm test.zip
fi
