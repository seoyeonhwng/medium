# bash 쉘로 실행
#!/bin/bash
set -e

# package 폴더가 존재하면 삭제
if [ -d "package" ]; then
    rm -rf package*
fi

# package 폴더 생성
mkdir package

# 활성화된 가상 환경을 package 폴더에 복사
cp -rf $(pipenv --venv)/lib/python3.7/site-packages/* package

# 제거해야 하는 라이브러리를 package 폴더에서 제거
rm -rf package/psycopg2
rm -rf package/psycopg2_*
rm -rf package/boto*

# 람다 실행시 필요한 파일을 package 폴더에 복사
cp *.py package
cp *.json package
cp *.csv package
cp *.txt package

# 람다 실행시 필요한 폴더를 package 폴더에 복사
cp -rf utils package
cp -rf sql package

# 입력받은 매개변수를 package 폴더에 복사
if [ $# -ne 0 ]; then
    cp "$@" package
fi

# package 폴더를 package.zip으로 압축 후 삭제
cd package
zip -rq ../package.zip .
cd ..
rm -rf package
