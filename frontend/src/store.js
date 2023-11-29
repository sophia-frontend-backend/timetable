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
        const response = await axios.get('http://127.0.0.1:5000/');
        commit('setClassInfo', response.data);
        console.log('データの取得が完了しました:', response.data);
      } catch (error) {
        console.error('データの取得に失敗しました:', error);
      }
    },
    async timeTableList({ state }) {
      return state.ClassInfo;
    },
    async getTable({ dispatch }) {
      try {
        // バックエンドからデータを取得
        await dispatch('fetchDataFromBackend');
      } catch (error) {
        console.error('データの取得に失敗しました:', error);
      }
    },
    async changeTable({ dispatch }, updatedData) {
      try {

        const { date, period } = updatedData;
        // PUTリクエストをバックエンドに送信
        await axios.put(`http://127.0.0.1:5000/timetable/${date}/${period}`, updatedData,{
          headers: {
              'Content-Type': 'application/json',  // 適切なContent-Typeを指定する
          }
      });
    
        // データが変更されたので、再度データを取得
        await dispatch('fetchDataFromBackend');
      } catch (error) {
        console.error('データの更新に失敗しました:', error);
      }
    },
    
    async deleteTable({ dispatch }, { date, period }) {
      try {
        // PUTリクエストをバックエンドに送信
        await axios.put(`http://127.0.0.1:5000/timetable/${date}/${period}`, {
          classname: '',
          professor: '',
          room: ''
        });
        
        // データが変更されたので、再度データを取得
        await dispatch('fetchDataFromBackend');
      } catch (error) {
        console.error('データの削除に失敗しました:', error);
      }
    },
    async deleteAllTable({ dispatch }) {
      try {
        const weekDays = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日'];
        const periods = [1, 2, 3, 4, 5, 6];
        // 表のセルをfor文で回して、各セルに対してPUTリクエストを行う
        for (const dateLabel of weekDays) {
          for (const period of periods) {
            await axios.put(`http://127.0.0.1:5000/timetable/${dateLabel}/${period}`, {
              classname: '',
              professor: '',
              room: ''
            })
          }
        }
        // データが更新されたので、表示上も更新
        await dispatch('fetchDataFromBackend');
      } catch (error) {
        console.error('データの更新に失敗しました:', error);
      }
    },
  }
});

export default store;
