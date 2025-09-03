const { Telegraf } = require('telegraf');
const { getAvailableGifts } = require('./getAvailableGifts');

const bot = new Telegraf(process.env.BOT_TOKEN);

function markGift(gift) {
  const emoji = gift.sticker?.emoji || '🎁';
  const base = `${emoji} ${gift.star_count}⭐`;
  return (gift.remaining_count !== undefined && gift.total_count !== undefined)
    ? base + ' 可升级'
    : base;
}

bot.command('gifts', async (ctx) => {
  try {
    const gifts = await getAvailableGifts();
    ctx.reply(gifts?.length ? gifts.map(markGift).join('\n') : 'No gifts available');
  } catch {
    ctx.reply('Error while getting gifts');
  }
});

bot.launch();
