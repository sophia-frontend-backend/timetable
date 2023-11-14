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
    async fetchClassInfo({ commit }) {
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
