def add_to_end(self, priority, name):
        new_job = Job(priority, name)
        self.heap.append(new_job)
        print(f"Added to the end: {new_job}")
def set_value_at_index(self, index, priority, name):
        new_job = Job(priority, name)
        if index < len(self.heap):
            self.heap[index] = new_job
            print(f"Updated index {index} with: {new_job}")
        else:
            while len(self.heap) < index:
                self.heap.append(None)
            self.heap.append(new_job)
            print(f"Placed new value at index {index}: {new_job}")
def bubble_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[parent].priority >= self.heap[i].priority:
                break
            self._swap(i, parent)
            i = parent

class Job:
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name
    def __str__(self):
        return f"Job(Name: '{self.name}', Priority: {self.priority})"
class MaxHeapScheduler:
    def __init__(self):
        self.heap = []
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    def insert(self, priority, name):
        new_job = Job(priority, name)
        self.heap.append(new_job)        
        current_index = len(self.heap) - 1
        while current_index > 0:
            parent = (current_index - 1) // 2
            if self.heap[parent].priority >= self.heap[current_index].priority:
                break
            self._swap(current_index, parent)
            current_index = parent    
        print(f"\n[Success] Added: {new_job}")
    def extract_max(self):
        if len(self.heap) == 0:
            return "Scheduler is empty!"
        if len(self.heap) == 1:
            return self.heap.pop()
        max_job = self.heap[0]
        self.heap[0] = self.heap.pop()  
        current_index = 0
        heap_size = len(self.heap)
        while True:
            left_child = 2 * current_index + 1
            right_child = 2 * current_index + 2
            largest = current_index
            if left_child < heap_size and self.heap[left_child].priority > self.heap[largest].priority:
                largest = left_child
            if right_child < heap_size and self.heap[right_child].priority > self.heap[largest].priority:
                largest = right_child
            if largest == current_index:
                break
            self._swap(current_index, largest)
            current_index = largest
        return max_job
    def peek(self):
        if len(self.heap) == 0:
            return "Scheduler is empty!"
        return self.heap[0]
    def display(self):
        if len(self.heap) == 0:
            print("\n[Info] Scheduler is currently empty.")
            return
        print("\n--- Current Jobs in Max Heap Order ---")
        for i, job in enumerate(self.heap):
            print(f"Index {i}: {job}")
        print("-----------------------------------------")
def main():
    scheduler = MaxHeapScheduler()
    while True:
        print("\n==============================")
        print("    MAX HEAP JOB SCHEDULER    ")
        print("==============================")
        print("1. Insert a Job")
        print("2. Extract Highest Priority Job (Process/Delete)")
        print("3. Peek at Highest Priority Job")
        print("4. Display All Jobs")
        print("5. Exit")   
        choice = input("\nEnter your choice (1-5): ").strip()
        if choice == '1':
            try:
                name = input("Enter Job Name: ").strip()
                priority = int(input("Enter Job Priority (Integer): "))
                scheduler.insert(priority, name)
            except ValueError:
                print("\n[Error] Priority must be a valid integer number!")
        elif choice == '2':
            result = scheduler.extract_max()
            print(f"\n[Processed] {result}")
        elif choice == '3':
            result = scheduler.peek()
            print(f"\n[Peek] Highest Priority Job: {result}")
        elif choice == '4':
            scheduler.display()
        elif choice == '5':
            print("\nExiting Job Scheduler. Goodbye!")
            break
        else:
            print("\n[Error] Invalid choice! Please enter a number between 1 and 5.")
if __name__ == "__main__":
    main()

