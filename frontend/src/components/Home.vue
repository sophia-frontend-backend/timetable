<template>

  <div class="table-container">
      <table class="table table-sm table-bordered">
        <thead>
          <tr>
            <th></th>
            <th v-for="dateLabel in weekDays" :key="dateLabel" class="cell-days">{{ dateLabel }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="period in periods" :key="period"  style="height: 120px;">
            <td class="cell-time">{{ period }}限
            </td>          

            <td v-for="dateLabel in weekDays" :key="dateLabel" @click="showEditForm(dateLabel, period)" class="hover-cell">
              <template v-if="getClassname(dateLabel, period)">
                <div class="class-name" v-if="getClassname(dateLabel, period).classname">
                  {{ ` ${getClassname(dateLabel, period).classname}` }}
                </div>        
                <div class="room-name" v-if="getClassname(dateLabel, period).room">
                  {{ `教室: ${getClassname(dateLabel, period).room}` }}
                </div>
                <div class="prof-name" v-if="getClassname(dateLabel, period).professor">
                  {{ `教授: ${getClassname(dateLabel, period).professor}` }}
                </div>
              </template>

            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="button">
      <button class="btn btn-danger m-3"  data-bs-toggle="modal" data-bs-target="#confirmationModal">全てのデータを削除</button>
    </div>
      <!-- 確認モーダル -->
    <div class="modal" tabindex="-1" id="confirmationModal">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">確認</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            本当にすべてのデータを削除しますか？
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-danger" data-bs-dismiss="modal">いいえ</button>
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" @click="deleteAllTable">はい</button>
          </div>
        </div>
      </div>
    </div>

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

 
<style scoped>
.table-container {
  margin: 0 auto;
  width: 800px; /* 適切な横幅に調整 */
  overflow-x: auto; /* テーブルの横幅がコンテナを超える場合にスクロールバーを表示 */
  background-image: url(../../timetable/imgs/logo.png);
}

 .hover-cell:hover{
  background-color: #e7e7e7;
  cursor: pointer;
 }
 .hover-cell {
  padding: 10px; 
  max-width: 100px;
  /* white-space: nowrap; テキストを折り返さないようにする */
  overflow: hidden; /* オーバーフローした部分を隠す */ 
  text-overflow: ellipsis; /* テキストがオーバーフローした場合に省略記号で表示 */
}
.hover-cell:not(:empty) {
  background-color: rgba(247, 198, 224, 0.35); /* 背景色と透明度を調整*/
}
.hover-cell .class-name {
  font-weight: bold;
  text-align: center;
}
.cell-time{
  width: 70px;
  text-align: center;
  white-space: nowrap;
}
.cell-days{
  width:200px;
  height:20px;
  white-space: nowrap;
}
.table th {
  text-align: center;
}
.room-name{
  text-align: center;
  font-size: 90%;
}
.prof-name{
  text-align: end;
  font-size: 90%;
}
.button{
  text-align: right;
}

</style>
