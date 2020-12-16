var getCaseInfo = function () {


    // 调用获取select数据列表
    $.get("/api/get_case_info/" + caseId + "/", {},
        function (resp) {
            if (resp.code == 10200) {
                console.log(resp.data.name);
                $("#req_url").val(resp.data.url);
                $("#case_name").val(resp.data.name);
                $("#result").val(resp.data.response);
                $("#assertContent").val(resp.data.response_assert);
                //回显请求方法
                if (resp.data.method == 1) {
                    $("#requestMethod").val("GET")
                } else if (resp.data.method == 2) {
                    $("#requestMethod").val("POST")
                } else {
                    alert("请求方法不支持显示")
                }
                //预设请求类型
                if (resp.data.request_type == 1) {
                    $('#data').prop('checked', true);
                } else if (resp.data.request_type == 2) {
                    $("#json").prop('checked', true);
                } else {
                    window.alert("不支持参数类型")
                }
                console.log("调用初始化列表");
                console.log("-->>>", resp.data.module);
                console.log("-->>>", resp.data.project);
                //预设项目-模块下拉
                SelectInit(resp.data.project, resp.data.module);
                //预设请求体
                var par_json = JSON.parse(resp.data.request_body);
                requestParam.set(par_json);


            } else {
                alert(resp.data);
            }
        }
    );
};
