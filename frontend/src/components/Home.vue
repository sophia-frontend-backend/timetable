<template>
  <div>
    <table>
      <thead>
        <tr>
          <th></th> <!-- 空のセル -->
          <th v-for="dateLabel in weekDays" :key="dateLabel">{{ dateLabel }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="period in periods" :key="period">
          <td>{{ period }}限</td>
          <td v-for="dateLabel in weekDays" :key="dateLabel" @click="showEditForm(dateLabel, period)">
            {{ getTableCellContent(dateLabel, period) }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import Delete from './Delete.vue';
import ChangeButton from './ChangeButton.vue';
import ChangeForm from './ChangeForm.vue';
import axios from 'axios';

export default {
  components: {
    Delete,
    ChangeButton,
    ChangeForm,
  },
  data() {
    return {
      showForm: false,
    };
  },
  computed: {
    ...mapState(['ClassInfo']),
    weekDays() {
      return ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日']; // 曜日のリスト
    },
    periods() {
      return [1, 2, 3, 4, 5, 6]; // 期間のリスト
    },
  },
  created() {
    this.fetchDataFromBackend(); // データをバックエンドから取得
  },
  methods: {
    ...mapActions(['fetchDataFromBackend']),
    async deleteClassInfo(date, period) {
      try {
        // バックエンドのAPIを呼び出してデータを削除
        const response = await axios.put(`http://127.0.0.1:5000/timetable/${date}/${period}`,
        {
          classname: '',
          professor: '',
          room: ''
        })
        console.log('データが削除されました:', response);
        
        // データが削除されたので、表示上も更新
        this.fetchDataFromBackend();
      } catch (error) {
        console.error('データの削除に失敗しました:', error);
      }
    },
    getTableCellContent(dateLabel, period) {
      // this.ClassInfo.timetabels が存在しているか確認
      if (this.ClassInfo && this.ClassInfo.timetabels) {
        const matchingInfo = this.ClassInfo.timetabels.find(
          info => info.date === dateLabel && info.period === period
        );
        return matchingInfo ? `${matchingInfo.classname} / ${matchingInfo.professor} / ${matchingInfo.room}` : '';
      } else {
        console.error('timetabels プロパティが存在しません');
        return ''; // エラーが発生した場合、空の文字列を返すなどの適切な処理を行う
      }
    },

    async updateClassInfo(updatedData) {
      // バックエンドのAPIを呼び出してデータを更新
      try {
        this.$route.push("/register")
        console.log("Hello")
        // const response = await axios.put(`http://127.0.0.1:5000/timetable/${updatedData.timetabels.date}/${updatedData.timetabels.period}`, updatedData);
        // console.log('データが更新されました:', response.data);

        // // データが更新されたので、表示上も更新
        // this.fetchDataFromBackend();
        // this.showForm = false; // フォームを非表示にする
      } catch (error) {
        console.error('データの更新に失敗しました:', error);
      }
    },
    showEditForm(date, period) {
      this.$router.push({path: "/register", query: {"date": date, "period": period}})
      this.showForm = true; // フォームを表示する
    },
  },
  watch: {
    // もしデータが変更されたらログを表示
    ClassInfo: {
      handler(newValue) {
        console.log('ClassInfo updated:', newValue);
      },
      deep: true,
    },
  },
};
</script>