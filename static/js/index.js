var table = document.getElementById("table-1");  // 表格
var input = document.getElementById("lin"); // 搜索框
input.onkeyup = function () {
   new Search(table, input)
}