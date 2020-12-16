var SelectInit = function (defaultProjectId, defaultModuleId) {

    var projectSelect = document.getElementById("projectSelect"); //项目选择框对象
    var moduleSelect = document.getElementById("moduleSelect"); //模块选择框对象
    var dataList = [];

    function addOption(cmb, obj) {
        var option = document.createElement("option"); //创建列表对象
        cmb.options.add(option); //选择框对象添加列表对象
        option.innerHTML = obj.name; //选项添加对象的名称
        option.value = obj.id; //选项value属性添加对象的id

    }

    function setDefaultOption(obj, id) {
        // console.log(id);
        for (let i = 0; i < obj.options.length; i++) {
            if (obj.options[i].value == id) {
                console.log(obj.options[i].value);
                obj.selectedIndex = i;
                return;
            }
        }
    }

    function changeProject() {
        moduleSelect.options.length = 0;
        var pid = projectSelect.options[projectSelect.selectedIndex].value;

        for (let i = 0; i < dataList.length; i++) {
            if (dataList[i].id == pid) {
                var modules = dataList[i].moduleList;
                for (var j = 0; j < modules.length; j++) {
                    addOption(moduleSelect, modules[j]);
                }
            }

        }

        setDefaultOption(moduleSelect, defaultModuleId);
    }

    function getSelectData() {
        $.post("/api/select_data/", {},
            function (resp) {
                if (resp.code == 200) {
                    dataList = resp.data;
                    for (let i = 0; i < dataList.length; i++) {
                        addOption(projectSelect, dataList[i]); //给项目选择框添加选项
                    }
                    setDefaultOption(projectSelect, defaultProjectId); //
                    changeProject();
                    projectSelect.onchange = changeProject;

                }
                setDefaultOption(projectSelect, defaultProjectId)
            }
        );
    }

    getSelectData();
};