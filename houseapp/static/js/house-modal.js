$(document).ready(function () {
  $('.tooltip-trigger').click(function () {
    // マウスが要素に入ったときの処理
    var tooltipContent = $(this).data('tooltip');
    $('#tooltip-content').html(tooltipContent);

    // マウスの位置を取得
    // var mouseX = event.clientX;
    // var mouseY = event.clientY;

    // モーダルをマウスの横に配置
    // $('#tooltip-modal').css({
    //   top: mouseY, // 上方向に10pxオフセット
    //   left: mouseX , // 右方向に10pxオフセット
    // });

    $('#tooltip-modal').fadeIn();
  });

  $('#close-modal').click(function () {
	$('#tooltip-modal').fadeOut();
  });
});
