function debounce(func, delay) {
  let timeoutId;
  return () => {
    if (timeoutId) {
      clearTimeout(timeoutId);
    }
    timeoutId = setTimeout(() => {
      func();
    }, delay);
  };
}

const log = debounce(() => console.log('Debounced!'), 1000);
log();
log();
log(); // 마지막 호출로부터 1초 후 "Debounced!" 출력
