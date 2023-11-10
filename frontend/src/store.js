import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    classInfo: [] // データを格納する配列
  },
  mutations: {
    setClassInfo(state, data) {
      state.classInfo = data;
    }
  },
  actions: {
    fetchClassInfo({ commit }) {
      // 同期的な処理でデータを取得するための関数
      const fetchData = async () => {
        try {
          const response = await axios.get('http://127.0.0.1:5000');
          console.log('データの取得が完了しました:', response.data);
          return response.data;
        } catch (error) {
          console.error('データの取得に失敗しました:', error);
          throw error; // エラーを再スローして呼び出し元で処理できるようにする
        }
      };

      // fetchClassInfo アクションを同期処理で実行
      try {
        const data = fetchData();
        commit('setClassInfo', data);
      } catch (error) {
        // エラーハンドリング
        // エラーが発生した場合の処理をここに追加
      }
    }
  }
});
