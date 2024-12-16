function qs(arr: number[], low: number, high: number): void {
  if (low >= high) {
    return
  }

  const pivotIndex = partition(arr, low, high)
  qs(arr, low, pivotIndex - 1)
  qs(arr, pivotIndex + 1, high)
}

function partition(arr: number[], low: number, high: number): number {
  const pivot = arr[high]
  let index = low - 1

  for (let i = low; i < high; i++) {
    if (arr[i] <= pivot) {
      index++
      const tmp = arr[i]
      arr[i] = arr[index]
      arr[index] = tmp
    }
  }

  index++
  arr[high] = arr[index]
  arr[index] = pivot

  return index
}

function quick_sort(arr: number[]): void {
  qs(arr, 0, arr.length - 1)
}

const sortable = [5, 2, 92, 87, 816, 77, 10, 8, 11, 64, 52]
quick_sort(sortable)
console.log(sortable);
