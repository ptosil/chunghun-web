// 공지사항 표시
fetch("notice.json")
  .then(res => res.json())
  .then(data => {
    const html = data.map(n => `
      <div class="bg-white rounded-xl shadow p-4 mb-4 text-left">
        <h3 class="text-lg font-bold text-blue-600">📢 ${n.title}</h3>
        <p>${n.content}</p>
        <p class="text-sm text-gray-400 mt-1">${n.date}</p>
      </div>
    `).join("");
    document.getElementById("notice-section").innerHTML = html;
  });

// 급식표 표시
fetch("lunch.json")
  .then(res => res.json())
  .then(data => {
    document.getElementById("lunch-section").innerHTML = `
      <div class="bg-white rounded-xl shadow p-4">
        <h2 class="text-xl font-bold text-blue-600">🍱 오늘의 급식</h2>
        <pre class="mt-2 text-left whitespace-pre-wrap">${data.meal}</pre>
      </div>`;
  });

// 시간표 표시
fetch("timetable.json")
  .then(res => res.json())
  .then(data => {
    let html = `<h2 class='text-xl font-bold text-blue-600 mb-2'>📅 시간표</h2>`;
    for (let day in data) {
      html += `<div class='mb-2'><strong>${day}요일:</strong> ${data[day].join(', ')}</div>`;
    }
    document.getElementById("timetable-section").innerHTML = html;
  });

// 학사일정 표시
fetch("calendar.json")
  .then(res => res.json())
  .then(data => {
    let html = `<h2 class='text-xl font-bold text-blue-600 mb-2'>📆 학사일정</h2>`;
    const keys = Object.keys(data);
    if (keys.length === 1 && data[keys[0]].includes("없습니다")) {
      html += `<div class='text-gray-500'>오늘은 학사일정이 없습니다.</div>`;
    } else {
      for (let date in data) {
        html += `<div class='mb-1'>${date} - ${data[date]}</div>`;
      }
    }
    document.getElementById("calendar-section").innerHTML = html;
  });

// 커뮤니티 구현
function savePost() {
  const text = document.getElementById("writeBox").value;
  if (!text) return;
  let posts = JSON.parse(localStorage.getItem("posts") || "[]");
  posts.unshift({ text, time: new Date().toLocaleString() });
  localStorage.setItem("posts", JSON.stringify(posts));
  document.getElementById("writeBox").value = "";
  showPosts();
}

function deletePost(index) {
  let posts = JSON.parse(localStorage.getItem("posts") || "[]");
  posts.splice(index, 1);
  localStorage.setItem("posts", JSON.stringify(posts));
  showPosts();
}

function showPosts() {
  let posts = JSON.parse(localStorage.getItem("posts") || "[]");
  const html = posts.map((p, i) => `
    <li class='flex justify-between items-center mb-1'>
      <span>${p.text} <small class='text-gray-400 ml-2'>${p.time}</small></span>
      <button onclick='deletePost(${i})' class='text-red-500 text-sm'>삭제</button>
    </li>`).join("");
  document.getElementById("community-section").innerHTML = `
    <div class='bg-white rounded-xl shadow p-4'>
      <h2 class='text-xl font-bold text-blue-600 mb-2'>💬 커뮤니티</h2>
      <textarea id='writeBox' class='w-full border p-2 rounded mb-2' placeholder='하고 싶은 말을 남겨보세요'></textarea>
      <button onclick='savePost()' class='bg-blue-500 text-white px-4 py-1 rounded'>글쓰기</button>
      <ul class='mt-4 text-left'>${html}</ul>
    </div>`;
}
document.addEventListener("DOMContentLoaded", showPosts);
