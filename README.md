# TON Coding Challenge 2025 Round 11

> 时间：2025/08/27 - 2025/09/06

为了帮助大家快速掌握 TON 生态的开发技能，我们特别设计了有趣的编程入门挑战赛。快来参与并有机会赢取 Telegram Premium 大会员！详细的比赛规则请查看群组公告。

https://t.me/toneachat

> 如何参与？
>
> Fork 本仓库的代码，回答下面的问题，然后发起一个 Pull Requests 就算成功参与。

---

课件地址：https://ton-org.notion.site/TG-Bot-API-for-Gifts-25a5274bd2cf80d7a642c7cf28a00d34

领奖信息收集：
1. 你的 Telegram 用户名 = @kooal111
2. 你的主网 TON 钱包地址 = UQAjKYAsbCbskV_DlGpaQtPpBv78Bo0iITVtAlvD1IU01kDa


## 任务 1：可升级礼物监听 bot 
### 任务描述：

1. 开发一个 bot，用户调用 /gifts 命令，则返回当前可购买的礼物
2. 当发现返回的礼物有限量礼物属性时候， 说明是一个可升级礼物，在礼物后面标注 “可升级”
3. 下面会附上一段限量礼物的 JSON 数据。

### 你的答案：

1. 将你的代码提交到本项目的根目录，文件名为 = upgradable_gifts_bot.py




下面的 JSON 数据是 getAvailableGifts 方法返回的部分信息，仅供参考。

```json
{
{
  id: '5882129648002794519',
  sticker: {
    width: 512,
    height: 512,
    emoji: '🎁',
    is_animated: true,
    is_video: false,
    type: 'custom_emoji',
    custom_emoji_id: '5305624709075864365',
    thumbnail: {
      file_id: 'AAMCAgADFQABaLUL2FRazld-e9vP2_oX-F87REUAAi2LAAKQXaFJ-99YygWf3LEBAAdtAAM2BA',
      file_unique_id: 'AQADLYsAApBdoUly',
      file_size: 2834,
      width: 128,
      height: 128
    },
    thumb: {
      file_id: 'AAMCAgADFQABaLUL2FRazld-e9vP2_oX-F87REUAAi2LAAKQXaFJ-99YygWf3LEBAAdtAAM2BA',
      file_unique_id: 'AQADLYsAApBdoUly',
      file_size: 2834,
      width: 128,
      height: 128
    },
    file_id: 'CAACAgIAAxUAAWi1C9hUWs5Xfnvbz9v6F_hfO0RFAAItiwACkF2hSfvfWMoFn9yxNgQ',
    file_unique_id: 'AgADLYsAApBdoUk',
    file_size: 39768
  },
  star_count: 2500,
  remaining_count: 46184,
  total_count: 50000
}
{
  id: '5170145012310081615',
  sticker: {
    width: 512,
    height: 512,
    emoji: '💝',
    is_animated: true,
    is_video: false,
    type: 'custom_emoji',
    custom_emoji_id: '5465263910414195580',
    thumbnail: {
      file_id: 'AAMCAgADFQABaLGSDtKKGxOJhCpNcl52LPIYcMIAAnwbAAKShNhL-K3EXM8imbUBAAdtAAM2BA',
      file_unique_id: 'AQADfBsAApKE2Ety',
      file_size: 6244,
      width: 128,
      height: 128
    },
    thumb: {
      file_id: 'AAMCAgADFQABaLGSDtKKGxOJhCpNcl52LPIYcMIAAnwbAAKShNhL-K3EXM8imbUBAAdtAAM2BA',
      file_unique_id: 'AQADfBsAApKE2Ety',
      file_size: 6244,
      width: 128,
      height: 128
    },
    file_id: 'CAACAgIAAxUAAWixkg7SihsTiYQqTXJedizyGHDCAAJ8GwACkoTYS_itxFzPIpm1NgQ',
    file_unique_id: 'AgADfBsAApKE2Es',
    file_size: 25528
  },
  star_count: 15
}
}

```







