def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    right = 0 #探索範囲の最初
    left = len(sorted_array)-1 #探索範囲の最後
    index = (right + left) // 2 #探索範囲の中間
    
    while(1):
        # targetがindexと一致する場合→indexを返す
        if sorted_array[index] == target_number:
            return index

        # targetがindexよりも後半にある場合→rightをずらす
        elif sorted_array[index] < target_number:
            right = index + 1
            index = (right + left) // 2

        # targetがindexよりも前半にある場合→leftをずらす
        elif sorted_array[index] > target_number:
            left = index - 1
            index = (right + left) // 2 

        # targetが見つからなかった場合→while文を抜ける      
        elif right >= left:
            break
        
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()