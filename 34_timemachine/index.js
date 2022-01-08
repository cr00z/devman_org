var TIMEOUT_IN_SECS = 3 * 60
var TEMPLATE = '<h1 style="margin:0px"><span class="js-timer-minutes">00</span>:<span class="js-timer-seconds">00</span></h1>'
var TIMER_STYLE = 'position:fixed; z-index:999999; top:25px; left:5px; padding:2px; border:2px double black; background-color:white;'

function padZero(number){
  return ("00" + String(number)).slice(-2);
}

class Timer{
  // IE does not support new style classes yet
  // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes
  constructor(timeout_in_secs){
    this.initial_timeout_in_secs = timeout_in_secs
    this.reset()
  }
  getTimestampInSecs(){
    var timestampInMilliseconds = new Date().getTime()
    return Math.round(timestampInMilliseconds/1000)
  }
  start(){
    if (this.isRunning)
      return
    this.timestampOnStart = this.getTimestampInSecs()
    this.isRunning = true
  }
  stop(){
    if (!this.isRunning)
      return
    this.timeout_in_secs = this.calculateSecsLeft()
    this.timestampOnStart = null
    this.isRunning = false
  }
  reset(timeout_in_secs){
    this.isRunning = false
    this.timestampOnStart = null
    this.timeout_in_secs = this.initial_timeout_in_secs
  }
  restart(timeout_in_secs){
    this.timestampOnStart = this.getTimestampInSecs()
    this.initial_timeout_in_secs = timeout_in_secs
    this.timeout_in_secs = timeout_in_secs
  }
  calculateSecsLeft(){
    if (!this.isRunning)
      return this.timeout_in_secs
    var currentTimestamp = this.getTimestampInSecs()
    var secsGone = currentTimestamp - this.timestampOnStart
    return Math.max(this.timeout_in_secs - secsGone, 0)
  }
}

class TimerWidget{
  // IE does not support new style classes yet
  // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes
  construct(){
    this.timerContainer = this.minutes_element = this.seconds_element = null
  }
  mount(rootTag){
    if (this.timerContainer)
      this.unmount()

    // adds HTML tag to current page
    this.timerContainer = document.createElement('div')

    this.timerContainer.setAttribute("style", TIMER_STYLE)
    this.timerContainer.innerHTML = TEMPLATE

    rootTag.insertBefore(this.timerContainer, rootTag.firstChild)

    this.minutes_element = this.timerContainer.getElementsByClassName('js-timer-minutes')[0]
    this.seconds_element = this.timerContainer.getElementsByClassName('js-timer-seconds')[0]
  }
  update(secsLeft){
    var minutes = Math.floor(secsLeft / 60);
    var seconds = secsLeft - minutes * 60;

    this.minutes_element.innerHTML = padZero(minutes)
    this.seconds_element.innerHTML = padZero(seconds)
  }
  unmount(){
    if (!this.timerContainer)
      return
    this.timerContainer.remove()
    this.timerContainer = this.minutes_element = this.seconds_element = null
  }
}

function randomSpeak(){
  var speaks = [
    "У Бога работа еще хуже, чем у тебя, и, увы, он даже не может уйти в отставку.",
    "Никогда не откладывай на завтра то, что может быть сделано послезавтра с тем же успехом.",
    "Вам кажется, что вы видите свет в конце тоннеля, а на самом деле это какой-то идиот с факелом, который принес вам еще больше работы.",
    "Это правда, что упорная работа никого не убила, но зачем рисковать?",
    "Если ежедневно работать по восемь часов в день, можно со временем стать начальником и работать по двенадцать часов в день.",
    "Работа — последнее прибежище тех, кто больше ничего не умеет.",
    "Большинство людей готово безмерно трудиться, лишь бы избавиться от необходимости немножко подумать.",
    "Я начал с нуля и упорным трудом достиг состояния крайней бедности.",
    "Работа — это иной раз нечто вроде рыбной ловли в местах, где заведомо не бывает рыбы.",
    "Сытый голодному не товарищ, а работодатель.",
    "Мне столько всего надо сделать, что лучше я пойду спать."
  ]
  return _.sample(speaks)
}

function main(){

  var timer = new Timer(TIMEOUT_IN_SECS)
  var timerWidget = new TimerWidget()
  var intervalId = null

  timerWidget.mount(document.body)

  function handleIntervalTick(){
    var secsLeft = timer.calculateSecsLeft()
    timerWidget.update(secsLeft)
    if (secsLeft === 0) {
      timer.restart(30)
      alert("Иди работай!\n" + randomSpeak())
    }
  }

  function handleVisibilityChange(){
    if (document.hidden) {
      timer.stop()
      clearInterval(intervalId)
      intervalId = null
    } else {
      timer.start()
      intervalId = intervalId || setInterval(handleIntervalTick, 300)
    }
  }

  // https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API
  document.addEventListener("visibilitychange", handleVisibilityChange, false);
  handleVisibilityChange()

}

if (document.readyState === "complete" || document.readyState === "loaded") {
  main();
} else {
  // initialize timer when page ready for presentation
  window.addEventListener('DOMContentLoaded', main);
}
