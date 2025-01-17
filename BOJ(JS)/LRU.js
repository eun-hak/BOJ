class LRUCache {
  constructor(capacity) {
    this.capacity = capacity;
    this.cache = new Map();
  }

  get(key) {
    if (!this.cache.has(key)) return -1;
    const value = this.cache.get(key);
    this.cache.delete(key);
    this.cache.set(key, value);
    return value;
  }

  put(key, value) {
    if (this.cache.has(key)) {
      this.cache.delete(key);
    }
    if (this.cache.size >= this.capacity) {
      const oldestKey = this.cache.keys().next().value;
      this.cache.delete(oldestKey);
    }
    this.cache.set(key, value);
  }
}

// 사용 예시
const cache = new LRUCache(2);
cache.put(1, 1); // 캐시: {1: 1}
cache.put(2, 2); // 캐시: {1: 1, 2: 2}
console.log(cache.get(1)); // 1
cache.put(3, 3); // 캐시: {1: 1, 3: 3} (2 제거)
console.log(cache.get(2)); // -1
console.log(cache.cache.keys().next().value);
