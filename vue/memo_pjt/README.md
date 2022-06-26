# memo 어플 만들기

1. front
   - component : memo, root 생성
   - 

2. back
   - axios 이용해서 서버와 연결

3. DB
   - sql 이용해서 서버 꺼져도 정보 저장 될 수 있도록 함
   
4. 문제점

   - `axios error request failed with status code 404`
     sql 에서 테이블 생성 후 axios를 통해 서버와 프론트를 연결했으나 저장된 데이터가 출력이 안됨...

   해결 방법 : vue.config.js 에 아래 주소 등록해줘야함 하.. 이걸로 삼십분 넘게 썼다...

   ``` js
   devServer:{
       proxy:{
         "/api":{
           target:"http://localhost:3000"
         }
       }
     }
   ```

   