(function(){const s=document.createElement("link").relList;if(s&&s.supports&&s.supports("modulepreload"))return;for(const e of document.querySelectorAll('link[rel="modulepreload"]'))n(e);new MutationObserver(e=>{for(const o of e)if(o.type==="childList")for(const c of o.addedNodes)c.tagName==="LINK"&&c.rel==="modulepreload"&&n(c)}).observe(document,{childList:!0,subtree:!0});function t(e){const o={};return e.integrity&&(o.integrity=e.integrity),e.referrerPolicy&&(o.referrerPolicy=e.referrerPolicy),e.crossOrigin==="use-credentials"?o.credentials="include":e.crossOrigin==="anonymous"?o.credentials="omit":o.credentials="same-origin",o}function n(e){if(e.ep)return;e.ep=!0;const o=t(e);fetch(e.href,o)}})();function l(){let i=window.scrollY;window.onscroll=function(){let s=window.scrollY,t=20;Math.abs(i-s)>t&&(i>s?(document.getElementById("mobile-menu").classList.remove("active"),window.scrollY>240?document.getElementById("main-menu").style.top="-132px":document.getElementById("main-menu").style.top="0"):(document.getElementById("mobile-menu").classList.add("active"),document.getElementById("main-menu").style.top="-220px"),i=s)}}function r(){const i=document.querySelector("#activateMenu"),s=document.querySelector("#layout-mobile-menu .close"),t=document.querySelector("#layout-mobile-menu");i.addEventListener("click",function(){t.classList.toggle("active"),setTimeout(()=>{t.classList.toggle("size")},100)}),s.addEventListener("click",function(){setTimeout(()=>{t.classList.remove("active")},300),t.classList.toggle("size")}),t.addEventListener("click",function(n){n.target.classList.contains("active")&&(setTimeout(()=>{t.classList.remove("active")},300),t.classList.toggle("size"))}),document.addEventListener("keydown",function(n){n.key==="Escape"&&t.classList.contains("active")&&(setTimeout(()=>{t.classList.remove("active")},300),t.classList.toggle("size"))})}l();r();
