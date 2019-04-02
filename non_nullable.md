> You are trying to add a non-nullable field [필드 이름] to register without a default


models.py
```python
class Register(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    company=models.CharField(max_length=30)
    office=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    tel=models.CharField(max_length=30)
```



이 오류는 DB를 수정한 경우 자주 발생합니다. 이번 경우는 address 필드를 수정하셨을 때, 기존에 존재하는 정보들을 어떻게 수정할 건지 정하지 않았기 때문에 발생합니다.


예를들어 원래 Register모델에 address field가 없었는데 이번에 address field를 새로 추가해 마이그레이션 할 때, 장고가 기존에 있었던 Register 정보들(existing row)에는 address field에 어떤 정보를 추가해야되나요? 라고 물어보는 겁니다.


해결방법은 두가지가 있는데요.


1) 첫번째는 Field에 default 값을 설정해주는 겁니다. 예를 들면

`CharField(default = "종로구 창신동")`

이렇게 설정한 후 마이그레이션 하면 기존에 있었던 Register object들의 주소는 전부 종로구 창신동으로 설정됩니다.


2) 두번째는 null을 허용해주는 겁니다.

`CharField(null=True)`
이렇게 설정한 후, 마이그레이션 하면 기존에 있었던 Register object들의 주소는 null이 됩니다.
