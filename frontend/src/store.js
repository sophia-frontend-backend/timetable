// データ｜"message"の中身がどのファイルでも使える
import { createStore } from 'vuex'

export const store = createStore({
    state:{
        product: []
    },
    mutations: {
        addProduct(state, product) {
            //productに"status"要素を追加した。
            //statusの初期値は'未購入'。これを'購入済み'に変更することで購入機能を実装。
            product.status = '未購入';
            state.product.push(product);
        },
      },     
    actions: {
        saveProductData({ commit }, product) {
            commit('addProduct', product);
        }
    },
    getters: {
        product: (state) => state.product,
    }
})