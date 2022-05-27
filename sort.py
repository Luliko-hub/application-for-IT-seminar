def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array
    
    # 配列の先頭を基準値とする
    pivot = array[0]

    # ここから記述
    left = 0 # 探索範囲の左端
    right = len(array)-1 # 探索範囲の右端
    search_end = False # 探索終了条件を満たしていればTrue
    
    while(1):
        while(1):
            # 基準値より大きい値が見つかればbreak
            if (array[left] >= pivot):
                break
            # 探索終了条件を満たせばbreak
            if left + 1 == right:
                search_end = True
                break
            left += 1 
            
        
        while(1):
            # 基準値未満の値が見つかればbreak
            if (array[right] < pivot):
                break
            # 探索終了条件を満たせばbreak
            if left + 1 == right:
                search_end = True
                break
            right -= 1 

        # 探索終了条件を満たしている場合、break
        if search_end:
            break

        array[left], array[right] = array[right], array[left]

    left = sort(array[: right]) 
    right = sort(array[right: ])

    # 配列全体のsortされた結果 = 左半分がsortされた結果 + 右半分がsortされた結果
    return left + right
    # ここまで記述

if __name__ == '__main__':
    main()