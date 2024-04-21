import {LitElement, html} from 'lit';
import * as Turbo from "@hotwired/turbo"

window.Turbo = Turbo

// let uid = {};

// fetch('/reloader')
// 	.then(r=>r.text())
// 	.then(v=>{
// 		uid.uid = v
// 	})

// setInterval(()=>{
// 	fetch('/reloader')
// 		.then(r=>r.text())
// 		.then(v=>{
// 			if (uid.uid!=v) {
// 				window.location.reload()
// 			}
// 		})
// }, 2000)
