// store.js
import { createStore } from 'vuex';
import axios from 'axios';

const store = createStore({
  state: {
    ClassInfo: [] // データを格納
  },
  mutations: {
    setClassInfo(state, data) {
      state.ClassInfo = data;
    }
  },
  actions: {
    async fetchDataFromBackend({ commit }) {
      try {
        const response = await axios.get('http://127.0.0.1:5000');
        commit('setClassInfo', response.data);
        console.log('データの取得が完了しました:', response.data);
      } catch (error) {
        console.error('データの取得に失敗しました:', error);
      }
    }
  }
});

export default store;
