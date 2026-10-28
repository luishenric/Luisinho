const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});const p=await b.newPage({viewport:{width:1600,height:1000}});
p.on('console',m=>console.log(m.text()));p.on('pageerror',e=>console.log('ERR',e.message));
await p.goto('file://'+process.cwd()+'/index.html');await p.waitForFunction('window.done===true',{timeout:60000});await p.waitForTimeout(500);
await p.screenshot({path:'caixa3d.png'});await b.close();})();
