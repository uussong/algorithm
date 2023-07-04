function solution(s) {
   const answer = (s.length === 4 || s.length === 6) && s == parseInt(s) ? true : false;
   return answer;
}