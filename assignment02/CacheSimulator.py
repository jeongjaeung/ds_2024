class CacheSimulator:
        def __init__(self, cache_slots): # 캐시 슬롯 수를 설정하고, 캐시 히트 횟수와 총 요청 횟수를 초기화
            self.cache_slots = cache_slots
            self.cache = []  
            self.cache_hit = 0 # cache hit : 참조하는 값이 캐시안에 있으면 해당 값을 캐시의 가장 최근 위치에 넣어준다.
            self.tot_cnt = 1 # total count : 총 요청 횟수 
        
        def do_sim(self, page): #캐시 시뮬레이션을 수행 #슬롯의 맨 뒤에 최근 데이터를 넣도록 함.
            if page in self.cache: #캐시안에 있는경우
                self.cache.remove(page) 
                self.cache.append(page)
                self.cache_hit += 1
            else:
                if len(self.cache) < self.cache_slots: #현재 캐시 메모리에 저장된 페이지의 수 < 캐시 메모리의 슬롯 개수 이면 "아직 여유 공간이 있다는 의미"
                    self.cache.append(page)
                else:
                    self.cache.pop(0) # 가장 오래된 요소를 제거
                    self.cache.append(page) 
            self.tot_cnt += 1 #캐시 시뮬레이션을 수행했으므로 +1
            
        def print_stats(self): #캐시 시뮬레이션 결과를 출력 #현재 캐시 슬롯 수, 캐시 히트 횟수, 그리고 히트 비율을 출력
            print("cache_slot = ", self.cache_slots, "cache_hit = ", self.cache_hit, "hit ratio = ", self.cache_hit / self.tot_cnt)

if __name__ == "__main__":

        data_file = open("/Users/jeongjaeung/Desktop/pythonpractice/ds-2024/assignment02/linkbench.trc")
        lines = data_file.readlines()
        for cache_slots in range(100, 1001, 100):
            cache_sim = CacheSimulator(cache_slots)
            for line in lines:
                page = line.split()[0]
                cache_sim.do_sim(page)
            
            cache_sim.print_stats()


    # cacheSize = 3
    # reference = [1, 2, 3, 4, 5, 6]
    # cache = []
    # for ref in reference:
    #   if not ref in cache:
    #     if len(cache) < cacheSize:
    #         cache.append(ref)
    #      else:
    #         cache.pop(0)
    #         cache.append(ref)
    #   else:
    #     cache.pop(cache.index(ref))
    #     cache.append(ref)
            

