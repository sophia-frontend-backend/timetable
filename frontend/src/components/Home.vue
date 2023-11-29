<template>
  <div>
    <table class="table table-sm table-bordered">
      <thead>
        <tr>
          <th></th>
          <th v-for="dateLabel in weekDays" :key="dateLabel">{{ dateLabel }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="period in periods" :key="period"  style="height: 100px;">
          <td>{{ period }}限</td>

          <td v-for="dateLabel in weekDays" :key="dateLabel" @click="showEditForm(dateLabel, period)">
            <template v-if="getClassname(dateLabel, period)">
              <div v-if="getClassname(dateLabel, period).classname">
                {{ `授業: ${getClassname(dateLabel, period).classname}` }}
              </div>
              <div v-if="getClassname(dateLabel, period).room">
                {{ `教室: ${getClassname(dateLabel, period).room}` }}
              </div>
              <div v-if="getClassname(dateLabel, period).professor">
                {{ `教授: ${getClassname(dateLabel, period).professor}` }}
              </div>
            </template>

          </td>
        </tr>
      </tbody>
    </table>
    <button class="btn btn-danger m-3" @click="deleteAllTable">全てのデータを削除</button>
  </div>
  <!-- {{ ClassInfo }} -->
</template>

<script>
import { mapState, mapActions } from 'vuex';
import axios from 'axios';

export default {
  data() {
    return {
      showForm: false,
      cellContents: {}, // 各セルの内容を保持するオブジェクト
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
    ...mapActions(['fetchDataFromBackend','deleteAllTable']),
    async fetchDataFromBackend() {},

    // 勝手に追加したから消して自分で作り直して良いよ -----------------------------
    getClassname(date, period) {      
      if (this.ClassInfo.timetabels && this.ClassInfo.timetabels.length > 0) {
        const targetClass = this.ClassInfo.timetabels.find(
            item => item.date === date && parseInt(item.period) === parseInt(period)
          );
        return targetClass
      } else {
        return null;
      }
    },
    // --------------------------------------------

    getTableCellContent(dateLabel, period) {
      return this.cellContents[`${dateLabel}-${period}`] || '';
    },
    updateCellContents() {
      // ClassInfoからセルの内容を更新
      if (this.ClassInfo && this.ClassInfo.timetabels) {
        this.cellContents = {};
        this.ClassInfo.timetabels.forEach((info) => {
          this.cellContents[`${info.date}-${info.period}`] = `${info.classname} / ${info.professor} / ${info.room}`;
        });
      }
    },
    async updateClassInfo(updatedData) {
      // バックエンドのAPIを呼び出してデータを更新
      try {
        this.$route.push('/register');
        
      } catch (error) {
        console.error('データの更新に失敗しました:', error);
      }
    },
    // クリックしたセルの既存情報を/ergisterに渡す
    showEditForm(date, period) {
      const clickedClassInfo = this.getClassname(date, period);
      const queryParams = { date, period, ...clickedClassInfo };
      
      this.$router.push({ path: '/register', query: queryParams });
      this.showForm = true; // フォームを表示する
    },
  },
  watch: {
    // もしデータが変更されたらログを表示
    ClassInfo: {
      handler(newValue) {
        console.log('ClassInfo updated:', newValue);
        this.updateCellContents(); // セルの内容を更新
      },
      deep: true,
    },
  },
};
</script>
