#include <stdio.h> 
#include <stdlib.h>

typedef int element;
typedef struct ListNode {
    element data;
    struct ListNode* link;
}ListNode;

ListNode* insert_first (ListNode* head, element data) {
    ListNode* node = (ListNode*)malloc(sizeof(ListNode));
    node->data = data;
    
    if (head == NULL) {
            head = node;
            node->link = head; 
    }
    else {
            node->link= head->link;
            head->link = node;
    }
    return head;
}

ListNode * insert_last(ListNode* head, element data) {
    ListNode* node = (ListNode*)malloc(sizeof(ListNode)); 
    node->data = data;
    
    if (head == NULL) {
        head = node;
        node->link = head; 
    }
    else {
            node->link= head->link;
            head->link = node;
            head = node; 
    }
    return head;
}

void insert (ListNode* head, ListNode* pre, element data) {
    ListNode* node = (ListNode*)malloc(sizeof(ListNode));
    node->data = data;
        
    if (head == NULL) {
        head = node;
        node->link = head;
    }
    else {
        node->link = pre->link;
        pre->link = node;
    }
}

void print_list (ListNode* head) {
    ListNode* p = head->link;

    if (head == NULL) return;
    do {
        printf("%d -> ", p->data);
        p = p->link;
    } while (p != head); 
    printf("%d\n", p->data);
    printf("\n");
}

typedef struct {
    int cache_slots;
    int cache_hit;
    int tot_cnt;
    int* cache;
} CacheSimulator;

void init_cache(CacheSimulator* cache_sim, int cache_slots) {
    cache_sim->cache_slots = cache_slots;
    cache_sim->cache_hit = 0;
    cache_sim->tot_cnt = 1;
    cache_sim->cache = (int*)malloc(cache_slots * sizeof(int));
}

void free_cache(CacheSimulator* cache_sim) {
    free(cache_sim->cache);
}

void do_sim(CacheSimulator* cache_sim, int page) {
    int i, j;
    int cache_hit = 0;

    for (i = 0; i < cache_sim->cache_slots; i++) {
        if (cache_sim->cache[i] == page) {
            cache_hit = 1;
            break;
        }
    }
    
    if (cache_hit) {
        for (j = i; j > 0; j--) {
            cache_sim->cache[j] = cache_sim->cache[j - 1];
        }
        cache_sim->cache[0] = page;
        cache_sim->cache_hit++;
    }

    else {
        for (j = cache_sim->cache_slots - 1; j > 0; j--) {
            cache_sim->cache[j] = cache_sim->cache[j - 1];
        }
        cache_sim->cache[0] = page;
    }

    cache_sim->tot_cnt++;
}

void print_stats(CacheSimulator* cache_sim) {
    printf("cache_slot = %d cache_hit = %d hit ratio = %f\n", cache_sim->cache_slots, cache_sim->cache_hit, (float)cache_sim->cache_hit / cache_sim->tot_cnt);
}


int main() {
    FILE* data_file;
    char* file_name = "/Users/jeongjaeung/Desktop/pythonpractice/ds-2024/assignment02/linkbench.trc";
    char line[256];
    int cache_slots;
    CacheSimulator cache_sim;

    data_file = fopen(file_name, "r");
    if (data_file == NULL) {
        fprintf(stderr, "Error opening file %s\n", file_name);
        return 1;
    }

    for (cache_slots = 100; cache_slots <= 1000; cache_slots += 100) {
        init_cache(&cache_sim, cache_slots);

        while (fgets(line, sizeof(line), data_file)) {
            int page;
            sscanf(line, "%d", &page);
            do_sim(&cache_sim, page);
        }
        print_stats(&cache_sim);

        free_cache(&cache_sim);

        rewind(data_file);
    }

        fclose(data_file);

    return 0;
}